"""
File Manager Studio
--------------------
A clean, professional Streamlit UI wrapped around a simple file
Create / Read / Update / Delete (CRUD) toolkit.

Run with:
    streamlit run file_manager_app.py
"""

import streamlit as st
from pathlib import Path
from datetime import datetime

# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="File Manager Studio",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# Styling
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .main { background-color: #0f1117; }

        .app-title {
            font-size: 2.1rem;
            font-weight: 800;
            background: linear-gradient(90deg, #7c3aed, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .app-subtitle {
            color: #9ca3af;
            font-size: 0.95rem;
            margin-top: -8px;
        }

        div[data-testid="stMetric"] {
            background: rgba(124, 58, 237, 0.08);
            border: 1px solid rgba(124, 58, 237, 0.25);
            border-radius: 12px;
            padding: 12px 16px;
        }

        .card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: 22px 24px;
            margin-bottom: 14px;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 600;
            border: 1px solid rgba(124, 58, 237, 0.4);
        }
        div.stButton > button:hover {
            border: 1px solid #7c3aed;
            color: #7c3aed;
        }

        section[data-testid="stSidebar"] {
            background: #12141c;
            border-right: 1px solid rgba(255,255,255,0.06);
        }

        .stAlert { border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# Working directory (sandboxed so the demo doesn't touch random paths)
# --------------------------------------------------------------------------
WORKDIR = Path("file_manager_storage")
WORKDIR.mkdir(exist_ok=True)


def full_path(name: str) -> Path:
    """Resolve a filename inside the sandboxed working directory."""
    return WORKDIR / name


def human_size(num_bytes: int) -> str:
    for unit in ["B", "KB", "MB", "GB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.0f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} TB"


def list_files():
    return sorted([p for p in WORKDIR.iterdir() if p.is_file()], key=lambda p: p.name.lower())


# --------------------------------------------------------------------------
# Sidebar navigation
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🗂️ File Manager Studio")
    st.caption("A tiny CRUD toolkit for local files")
    st.divider()

    page = st.radio(
        "Operation",
        ["🏠 Dashboard", "📄 Create", "📖 Read", "✏️ Update", "🗑️ Delete"],
        label_visibility="collapsed",
    )

    st.divider()
    files_now = list_files()
    st.metric("Files stored", len(files_now))
    total_size = sum(f.stat().st_size for f in files_now)
    st.metric("Total size", human_size(total_size))

    st.divider()
    st.caption(f"Sandbox folder: `{WORKDIR}/`")

# --------------------------------------------------------------------------
# Header
# --------------------------------------------------------------------------
st.markdown('<p class="app-title">File Manager Studio</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="app-subtitle">Create, read, update and delete files — with a UI instead of a terminal prompt.</p>',
    unsafe_allow_html=True,
)
st.write("")

# --------------------------------------------------------------------------
# DASHBOARD
# --------------------------------------------------------------------------
if page == "🏠 Dashboard":
    files = list_files()

    if not files:
        st.info("No files yet — head to **Create** to add your first one.")
    else:
        st.markdown("#### Your files")
        for f in files:
            stat = f.stat()
            c1, c2, c3, c4 = st.columns([4, 2, 2, 1])
            c1.write(f"📄 **{f.name}**")
            c2.write(human_size(stat.st_size))
            c3.write(datetime.fromtimestamp(stat.st_mtime).strftime("%b %d, %Y %H:%M"))
            with c4:
                st.button("👁️", key=f"peek_{f.name}", help="Preview", on_click=lambda f=f: st.session_state.update(preview=f.name))

        if "preview" in st.session_state:
            p = full_path(st.session_state["preview"])
            if p.exists():
                st.markdown("---")
                st.markdown(f"**Preview: `{p.name}`**")
                try:
                    st.code(p.read_text(errors="replace")[:3000] or "(empty file)")
                except Exception as e:
                    st.error(f"Could not preview file: {e}")

# --------------------------------------------------------------------------
# CREATE
# --------------------------------------------------------------------------
elif page == "📄 Create":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Create a new file")

    name = st.text_input("File name", placeholder="notes.txt")
    content = st.text_area("Content", height=200, placeholder="Type what you want to write...")

    if st.button("Create file", type="primary"):
        if not name.strip():
            st.warning("Please enter a file name.")
        else:
            path = full_path(name.strip())
            if path.exists():
                st.error(f"'{name}' already exists. Try a different name.")
            else:
                try:
                    path.write_text(content)
                    st.success(f"✅ '{name}' created successfully!")
                    st.balloons()
                except Exception as err:
                    st.error(f"An error occurred: {err}")
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------------------------------
# READ
# --------------------------------------------------------------------------
elif page == "📖 Read":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Read a file")

    files = list_files()
    if not files:
        st.info("No files available. Create one first.")
    else:
        choice = st.selectbox("Choose a file", [f.name for f in files])
        if st.button("Read file", type="primary"):
            path = full_path(choice)
            try:
                text = path.read_text(errors="replace")
                st.success(f"Showing contents of '{choice}'")
                st.code(text if text else "(this file is empty)")
            except Exception as err:
                st.error(f"An error occurred: {err}")
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------------------------------
# UPDATE
# --------------------------------------------------------------------------
elif page == "✏️ Update":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Update a file")

    files = list_files()
    if not files:
        st.info("No files available. Create one first.")
    else:
        choice = st.selectbox("Choose a file", [f.name for f in files])
        operation = st.radio(
            "What do you want to do?",
            ["Rename", "Append content", "Overwrite content"],
            horizontal=True,
        )
        path = full_path(choice)

        if operation == "Rename":
            new_name = st.text_input("New file name")
            if st.button("Rename", type="primary"):
                if not new_name.strip():
                    st.warning("Please enter a new file name.")
                else:
                    new_path = full_path(new_name.strip())
                    if new_path.exists():
                        st.error("A file with that name already exists.")
                    else:
                        try:
                            path.rename(new_path)
                            st.success(f"✅ Renamed to '{new_name}'")
                        except Exception as err:
                            st.error(f"An error occurred: {err}")

        elif operation == "Append content":
            data = st.text_area("Text to append", height=150)
            if st.button("Append", type="primary"):
                try:
                    with open(path, "a") as fs:
                        fs.write(data)
                    st.success("✅ Content appended successfully!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

        elif operation == "Overwrite content":
            data = st.text_area("New content (replaces everything)", height=150)
            if st.button("Overwrite", type="primary"):
                try:
                    with open(path, "w") as fs:
                        fs.write(data)
                    st.success("✅ File overwritten successfully!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------------------------------
# DELETE
# --------------------------------------------------------------------------
elif page == "🗑️ Delete":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Delete a file")

    files = list_files()
    if not files:
        st.info("No files available to delete.")
    else:
        choice = st.selectbox("Choose a file", [f.name for f in files])
        confirm = st.checkbox(f"I understand this will permanently delete '{choice}'")
        if st.button("Delete file", type="primary", disabled=not confirm):
            try:
                full_path(choice).unlink()
                st.success(f"✅ '{choice}' deleted successfully!")
                st.rerun()
            except Exception as err:
                st.error(f"An error occurred: {err}")
    st.markdown("</div>", unsafe_allow_html=True)
