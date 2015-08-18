# -*- mode: ruby -*-
# # vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.ssh.insert_key = false

  if Vagrant.has_plugin?("vagrant-hostmanager")
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    config.hostmanager.ignore_private_ip = false
    config.hostmanager.include_offline = true
  end

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :machine
  end

  config.vm.define "retail" do |vmconfig|
    vmconfig.vm.box = "chef/centos-6.6"
    vmconfig.vm.provider "virtualbox" do |v|
      v.memory = 4096
      v.cpus = `#{RbConfig::CONFIG['host_os'] =~ /darwin/ ? 'sysctl -n hw.ncpu' : 'nproc'}`.chomp
    end

    vmconfig.vm.hostname = "retail.vagrant"
    vmconfig.vm.network :private_network, ip: "192.168.56.42"
     
    vmconfig.vm.provision "ansible" do |ansible|
      ansible.playbook = "mba_n1ql.yml"
    end
  end
end
