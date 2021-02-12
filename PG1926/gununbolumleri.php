<?php
date_default_timezone_set('Europe/Istanbul');
$saat=strftime('Saat: %H:%M');

if($saat>06.00 and $saat<=10.00){
    echo $saat," ","Günaydın";
}
else if($saat>10.00 and $saat<=17.00){
    echo $saat," ","İyi Günler";
}
else if ($saat>17.00 and $saat<=20.00){
    echo $saat," ","İyi Akşamlar";
}
else if ($saat>20.00 and $saat<=00.00){
    echo $saat," ","İyi Geceler";
}
else{
     echo $saat," ","Esenlikler Dilerim";
}
   
?>