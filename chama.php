<?php

$comando = escapeshellcmd('tap.py');
$cmdResult = shell_exec($comando);
echo $cmdResult;

?>