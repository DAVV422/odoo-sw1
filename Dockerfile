FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libpq-dev \
    git \
    libevent-dev \
    python3-setuptools \
    python3-pip \
    python3-wheel \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create odoo user and necessary directories
RUN useradd -ms /bin/bash odoo \
    && mkdir -p /opt/odoo /var/lib/odoo /etc/odoo \
    && chown -R odoo:odoo /var/lib/odoo /etc/odoo /opt/odoo

# Set working directory
WORKDIR /opt/odoo

# Copy repository contents
COPY --chown=odoo:odoo . .

# Create and activate virtual environment
RUN python -m venv /opt/odoo/venv
ENV PATH="/opt/odoo/venv/bin:$PATH"

# Upgrade pip and install wheel
RUN pip install --upgrade pip setuptools wheel

# Pre-install specific versions of problematic packages
RUN pip install --no-cache-dir \
    cython==0.29.32 \
    greenlet==2.0.2 \
    gevent==22.10.2

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set permissions
RUN chown -R odoo:odoo /opt/odoo

# Switch to odoo user
USER odoo

# Expose ports
EXPOSE 8069

# Set default command
CMD ["python", "odoo-bin", "--conf=/etc/odoo/odoo.conf"]