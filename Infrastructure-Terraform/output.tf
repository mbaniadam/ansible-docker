output "server_status" {
  value = hcloud_server.mpvps.status
}

output "server_ip" {
  value = hcloud_server.mpvps.ipv4_address
}

output "inventory" {
  value = data.template_file.inventory.rendered  
}