[machines]
%{ for ip in [ip_addresses] ~}
${ip} ansible_user=root
%{ endfor ~}
