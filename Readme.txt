This Project will check Tape on single Tape Library and will alert if tape is full

1. First Step you need to set postgres sql config "listen_addresses= {* or your backup ip}, 
because netvault backup server not allow remote connection to db (On my version postgres config store on C:\Program Files\Quest\NetVault Backup\db\pgsql\postgresql.conf)