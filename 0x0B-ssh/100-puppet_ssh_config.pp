# 100-puppet_ssh_config.pp

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}
