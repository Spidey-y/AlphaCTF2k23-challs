<?php
error_reporting(0);
error_log(0);

if (isset($_GET["h3lp"])) {
    highlight_file(__FILE__);
    exit;
}

if (isset($_POST["password"]) && !empty($_POST["password"]) && isset($_POST["username"]) && !empty($_POST["username"])) {
    $password = $_POST["password"];
    $username = $_POST["username"];
    if ($username == "4dm1n" && md5($password) == "0e953532678923638053842468642408") {
        if ( isset($_POST['flag']) ){
            require('flag.php');
            if ( strcmp( $_POST['flag'], $flag ) == 0 ){
                echo("You got it! That's the correct flag! <br>");
                echo("<h3>".$flag."</h3>");
                exit;
            }else{
                header("location: index.php?error=Nope! wrong flag.");
            }
        }
    } else {
        header("location: index.php?error=Incorrect password");
    }
}

?>

<!DOCTYPE html>
<html>

<head>
    <title>Php is good</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        .header {
            background-color: #000;
            color: #fff;
            padding: 10px;
            text-align: center;
            margin-bottom: 50px;
        }

        .error {
            background-color: #ff0000;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

    </style>
</head>

<body>
    <div class="header">
        <h1>PHP is GOOD</h1>
        <!-- <a href="index.php?h3lp">get help</a> -->
    </div>
    <div class="container">
        <?php
        if (isset($_GET["error"])) {
            echo "<div class='error'>" . $_GET["error"] . "</div>";
        }
        ?>
        <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="post" enctype="multipart/form-data"
            class="form-control">
            <label for="username">Username:</label>
            <input type="text" name="username" class="form-control">
            <label for="password">Password:</label>
            <input type="password" name="password" class="form-control">
            <label for="flag">flag:</label>
            <input type="text" name="flag" class="form-control">
            <input type="submit" value="Login" class="btn btn-primary" style="margin-top: 20px;">
        </form>
    </div>
</body>

</html>