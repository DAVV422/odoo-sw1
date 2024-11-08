# Dockerfile
FROM python:3.10-slim-buster

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
    && rm -rf /var/lib/apt/lists/*

# Create odoo user
RUN useradd -ms /bin/bash odoo

# Create necessary directories
RUN mkdir -p /opt/odoo /var/lib/odoo /etc/odoo
RUN chown odoo:odoo /var/lib/odoo /etc/odoo

# Set working directory
WORKDIR /opt/odoo

# Copy repository contents
COPY --chown=odoo:odoo . .

# Copy configuration file
COPY --chown=odoo:odoo odoo-example.conf /etc/odoo/odoo.conf

# Install Python dependencies
RUN python -m venv /opt/odoo/venv
ENV PATH="/opt/odoo/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Set permissions
RUN chown -R odoo:odoo /opt/odoo

# Switch to odoo user
USER odoo

# Expose Odoo port
EXPOSE 8069

# Set default command
CMD ["python", "odoo-bin", "--conf=/etc/odoo/odoo.conf"]