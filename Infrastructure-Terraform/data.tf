data "template_file" "inventory" {
    template = file("ansible_inventory.tpl")
    vars = {
      ip_addresses = hcloud_server.mpvps.ipv4_address
    }
}