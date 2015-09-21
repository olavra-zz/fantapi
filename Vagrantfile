# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8080, host: 8080  # jenkins
  config.vm.network "forwarded_port", guest: 8000, host: 8000  # django
  config.vm.network "private_network", ip: "10.10.10.10"
  # config.vm.network "public_network"
  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
  #  vb.gui = true
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
    echo 'deb http://pkg.jenkins-ci.org/debian binary/' >> /etc/apt/sources.list
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install jenkins python-dev python-pip libxml2-dev libxslt-dev libffi-dev lib32z1-dev
    sudo pip install -r /vagrant/fanapi/requirements
  SHELL
end
