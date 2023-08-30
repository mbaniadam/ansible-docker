terraform {
  required_providers {
    hcloud = {
      source = "hetznercloud/hcloud"
      version = "1.42.1"
    }
  }
}


# Configure the Hetzner Cloud Provider
provider "hcloud" {
  token = var.token
}