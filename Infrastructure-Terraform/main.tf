# Create a new SSH key
resource "hcloud_ssh_key" "default" {
  name       = "hetzner-ssh-key"
  public_key = file("~/.ssh/id_rsa.pub")
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


resource "local_file" "create_ansible_inventory_file" {
      content = "${data.template_file.inventory.rendered}"
      filename =  "Ansible-Configure/inventory.yml"  
}

resource "terraform_data" "run_ansible" {
    provisioner "local-exec" {
        command = "ansible-playbook -i Ansible-Configure/inventory.yml Ansible-Configure/docker-playbook.yml"
    } 
}

