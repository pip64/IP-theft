<?php
$fp = fopen("ips.txt", "a+");

function getIp() {
  $keys = [
    'HTTP_CLIENT_IP',
    'HTTP_X_FORWARDED_FOR',
    'REMOTE_ADDR'
  ];
  foreach ($keys as $key) {
    if (!empty($_SERVER[$key])) {
      $ip = trim(end(explode(',', $_SERVER[$key])));
      if (filter_var($ip, FILTER_VALIDATE_IP)) {
        return $ip;
      }
    }
  }
}

$ip = getIp();
// выведем IP клиента на экран

echo 'You are trolled! :)' . $ip;
fwrite($fp, "IP: " . $ip . "\n" . "\n");
fclose($fp);

?>
