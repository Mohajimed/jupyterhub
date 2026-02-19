from dockerspawner import DockerSpawner
from jupyterhub.auth import DummyAuthenticator

c = get_config()

# bind inside container
c.JupyterHub.bind_url = "http://:8000"

# simple login for testing (same password for all users)
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = "CHANGE_ME_PASSWORD"

# optional: admin user name
c.Authenticator.admin_users = {"admin"}

# spawn notebooks as docker containers
c.JupyterHub.spawner_class = DockerSpawner

# notebook image for each user
c.DockerSpawner.image = "jupyter/datascience-notebook:latest"

# container naming
c.DockerSpawner.name_template = "jhub-{username}"

# persistent storage per user
c.DockerSpawner.volumes = {
    "jhub-user-{username}": "/home/jovyan/work"
}

# limits (optional but recommended)
c.DockerSpawner.mem_limit = "1G"
c.DockerSpawner.cpu_limit = 1.0

# network (usually OK)
c.DockerSpawner.network_name = "bridge"
