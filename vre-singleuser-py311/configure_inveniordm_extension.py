import os

def configure_inveniordm_extension(config: dict):
    """
    Update the jupyter server configuration with settings for the InvenioRDM extension.
    """
    config["InvenioRDMJupyterLab"] = {
        "remote_servers": {
            "zenodo_production": {
                "label": "Zenodo",
                "base_url": "https://zenodo.org",
                "oauth_client_id": os.getenv("ZENODO_OAUTH_CLIENT_ID", "HaWBPRb7lsif7cqTypUNeFni9PJOoTm5IcjTJrtt"),
            },
            "cds_repository": {
                "label": "CDS",
                "base_url": "https://repository.cern",
                "oauth_client_id": os.getenv("CDS_OAUTH_CLIENT_ID", "q4szrkotZqAuRA6HhGeajJsqTqEd6t6lTHHGLWD4"),
            },
            "zenodo_sandbox": {
                "label": "Zenodo Sandbox",
                "base_url": "https://sandbox.zenodo.org",
                "oauth_client_id": os.getenv("ZENODO_SANDBOX_OAUTH_CLIENT_ID", "ca8NzRHmqp6tVA0IE9XUlmbL74cGm9RqguC9DZlU"),
            },
        }
    }