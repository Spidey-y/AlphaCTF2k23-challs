<?php 
    $flag="AlphaCTF{7hanK_G0D_7HIs_15_NO7_AvA1lAbLe_1N_n3W3r_vErSIOns}"; 
    if (isset($_GET['src'])) {
        if (strpos($_GET['src'], "?") !== FALSE) {
            echo 'hmmm';
            die();
        }
    }
?>  

my name is:
<?php
include "data://text/plain;base64,".base64_encode($_GET['src']);
?>