<?php

if(isset($_GET['target']) && isset($_GET['type']) && !empty($_GET['target'])){
	if ($_GET['type']=="ip" && filter_var($_GET['target'], FILTER_VALIDATE_IP)) {
		$ip_address=$_GET['target'];	
	}else if($_GET['type']=="website" && preg_match("/[a-zA-Z0-9]{1,30}\.[a-zA-Z0-9]{2,6}/",$_GET['target'],$tar_arr)){
		$addressArry=getAddresses_www($tar_arr[0]);
		if(!empty($addressArry) && !empty($tar_arr[0])){
			$ip_address=$addressArry[0];
		}else{
			echo "not a valid website!";
		}
	}else {
		exit(htmlentities($_GET['target'])." is not a valid ".htmlentities($_GET['type']));
	}
	
	if(isset($ip_address)){
		if (file_exists("result.txt")) {
			unlink("result.txt") or die("Couldn't delete result.txt");
		}
		system("python ghaniScan.py ".$ip_address,$ret);
		exit(file_get_contents("result.txt"));	
	}
	
	
}else{
	exit("please enter an ip address or website...");
}



function getAddresses($domain) {
  $records = dns_get_record($domain);
  $res = array();
  foreach ($records as $r) {
    if ($r['host'] != $domain) continue; // glue entry
    if (!isset($r['type'])) continue; // DNSSec

    if ($r['type'] == 'A') $res[] = $r['ip'];
    //if ($r['type'] == 'AAAA') $res[] = $r['ipv6'];
  }
  return $res;
}

function getAddresses_www($domain) {
  $res = getAddresses($domain);
  if (count($res) == 0) {
    $res = getAddresses('www.' . $domain);
  }
  return $res;
}

