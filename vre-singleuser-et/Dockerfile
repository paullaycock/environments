ARG BASE_IMAGE=ghcr.io/vre-hub/vre-singleuser-py311:latest
FROM ${BASE_IMAGE}
LABEL author="Paul Laycock"
LABEL maintainer="Paul Laycock <paul.laycock@unige.ch>"
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE

# eMudhra/emSign CA incident (October 2026): the emSign root was removed from
# the OS and Python trust stores. Refresh every copy the image carries:
# the Ubuntu bundle, conda's certifi and conda itself, and pip's vendored one.
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends --only-upgrade ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Replace the base image's Rucio extension config script with the
# env-driven ET version (see the header of configure-rucio.py).
COPY configure-rucio.py /usr/local/bin/configure-vre.py
RUN chmod 755 /usr/local/bin/configure-vre.py

# The extension's kernel module, importable from every kernel (conda envs
# included). Copied under its own name so it cannot shadow the server's
# rucio_jupyterlab package; configure-rucio.py registers it with IPython.
RUN d=$(python -c "import os, rucio_jupyterlab.kernels.ipython as m; print(os.path.dirname(m.__file__))") \
    && mkdir -p /opt/rucio-kernel-ext/rucio_jupyterlab_kernel \
    && cp "$d"/__init__.py "$d"/types.py /opt/rucio-kernel-ext/rucio_jupyterlab_kernel/
ENV PYTHONPATH=/opt/rucio-kernel-ext${PYTHONPATH:+:$PYTHONPATH}

# conda and pip run as the notebook user, who owns /opt/conda, as in the base image.
USER $NB_UID
RUN mamba install -y -n base -c conda-forge "certifi>=2026.10.19" "conda>=26.9.4" \
    && mamba clean -afy
RUN python -m pip install --upgrade "pip>=26.2.2" "certifi>=2026.10.19" \
    && python -m pip install nopayloaddb-client==0.3.0
