from dockerspawner import DockerSpawner
from jupyterhub.auth import DummyAuthenticator

c = get_config()

# Hub listens inside the container
c.JupyterHub.bind_url = "http://:8000"

# --- AUTH (testing only) ---
# Same password for all users (good for quick test).
# Replace later with GitHub/Google OAuth.
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = __import__("os").environ.get("JHUB_DUMMY_PASSWORD", "CHANGE_ME_PASSWORD")

# Make an admin user (optional)
c.Authenticator.admin_users = {"admin"}

# --- SPAWNER: one Docker container per user ---
c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.image = "jupyter/datascience-notebook:latest"
c.DockerSpawner.name_template = "jhub-{username}"

# Persist each user's notebooks in a dedicated Docker volume
c.DockerSpawner.volumes = {
    "jhub-user-{username}": "/home/jovyan/work"
}

# Limits (optional but recommended)
c.DockerSpawner.mem_limit = "1G"
c.DockerSpawner.cpu_limit = 1.0

# Usually fine on a single Docker host
c.DockerSpawner.network_name = "bridge"
