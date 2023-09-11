terraform {
  required_providers {
    hcloud = {
      source = "hetznercloud/hcloud"
      version = "1.42.1"
    }
    template = {
      source = "hashicorp/template"
      version = "2.2.0"
    }
  }
}


# Configure the Hetzner Cloud Provider
provider "hcloud" {
  token = var.token
}

provider "template" {
  # Configuration options
}