# Create a new SSH key
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "hcloud_ssh_key" "default" {
  name       = "hetzner-ssh-key"
  public_key = tls_private_key.ssh_key.public_key_openssh
}

resource "hcloud_server" "mpvps" {
  name        = "mpvps"
  image       = var.os_type
  server_type = var.server_type
  location    = var.location
  ssh_keys    = [hcloud_ssh_key.default.id]
}

resource "hcloud_network" "hcloud_network" {
  name     = "hetzner-cloud network"
  ip_range = var.ip_range
}

resource "hcloud_network_subnet" "hcloud_subnet" {
  network_id   = hcloud_network.hcloud_network.id
  type         = "cloud"
  network_zone = "eu-central"
  ip_range     = var.ip_range
}

resource "hcloud_server_network" "vpn_network" {
  server_id = hcloud_server.mpvps.id
  subnet_id = hcloud_network_subnet.hcloud_subnet.id
}