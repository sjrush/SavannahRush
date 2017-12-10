
<?php

$url = 'http://raspberrypi.local:5000/getLocked';
$results = file_get_contents($url);
echo $url;
echo $results;
?>
