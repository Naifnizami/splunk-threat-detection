<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);

    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        header("Location: upload_success.php");
        exit();
    } else {
        echo "File upload failed.";
    }
}
?>

<h2>Upload Your Documents</h2>
<form action="upload.php" method="post" enctype="multipart/form-data">
  Select file to upload:<br>
  <input type="file" name="fileToUpload" id="fileToUpload"><br><br>
  <input type="submit" value="Upload File" name="submit">
</form>
