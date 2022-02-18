<?php
$fp = fopen("ips.txt", "a+");
echo "<link rel='stylesheet' href='style.css'>";

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

fwrite($fp, "IP: " . $ip . "\n" . "\n");
fclose($fp);

echo '<h1>You are trolled. ' . $ip . '</h1>';
echo '<h1><img src = "https://media0.giphy.com/media/amxLHEPgGDCKs/200.gif"></h1>';
echo '<h1>Do you want to hide your ip from me?</h1>';
echo '<form action="troll.php" target="_blank"><button>Yes</button></form>'
?>

