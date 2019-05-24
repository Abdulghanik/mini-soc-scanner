<?php
$file = 'result.txt'; // example
$filesize=filesize($file);

if ($filesize > 0) {
header("Pragma: public"); // required
header("Expires: 0");
header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
header("Cache-Control: private",false); // required for certain browsers 
header("Content-Type: image/gif");
header("Content-Length: ".filesize($file));
header("Content-Disposition: attachment; filename=\"".basename($file)."\";" );

readfile($file);
}

?>