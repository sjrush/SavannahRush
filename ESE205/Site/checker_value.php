<html>
 <body>
<?php

echo "Your door will now ". $_POST["lock"]. "!<br>" ;

 $data1 = $_POST['lock'];
 $fileString = "$data1";
 $outputfile = 'doorstatus.txt';


 $ret=file_put_contents($outputfile, $fileString);

?>
 </body>
 </html>
