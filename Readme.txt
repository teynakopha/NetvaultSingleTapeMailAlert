This Project will check Tape on single Tape Library and will alert if tape is full or not enough for saturday and sunday

1. First Step you need to set postgres sql config "listen_addresses= {* or your backup ip}, 
    because netvault backup server not allow remote connection to db 
    (On my version postgres config store on C:\Program Files\Quest\NetVault Backup\db\pgsql\postgresql.conf)

2. then you need to set allow remote connection from another host 
    C:\Program Files\Quest\NetVault Backup\db\pgsql\pg_hba.conf

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
host    all             all             {your cidr}             md5
