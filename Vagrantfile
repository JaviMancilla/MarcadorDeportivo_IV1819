Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Variables correspondientes a la creacion de la MV
    azure.vm_name = "marcador-deportivo-18-19"
    azure.vm_size = "Standard_D2_v2"
    azure.tcp_endpoints = "80"
    azure.location = "westeurope"
    azure.admin_username = "javimancilla"


  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end
