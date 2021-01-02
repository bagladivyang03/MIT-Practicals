<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>updatedinfo</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,300;1,500;1,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="name">
                <h1>Library Management System</h1>
            </div>
            <nav class="navbar">
                <ul class="user-nav">
                    <li class="user-nav__item">
                    <li class="user-nav__item">
                        <a href="displaybooks.php" class="user-nav__link">
                            View Books
                        </a>
                    </li>
                        <a href="bookform.php" class="user-nav__link">
                            Add
                        </a>
                    </li>
                    <li class="user-nav__item">
                        <a href="deletebook.php" class="user-nav__link">
                            Delete
                        </a>
                    </li>
                    <li class="user-nav__item">
                        <a href="searchbooks.php" class="user-nav__link">
                            Search
                        </a>
                    </li>
                    <li class="user-nav__item">
                        <a href="updatebooks.php" class="user-nav__link">
                            Update
                        </a>
                    </li>
                </ul>
            </nav>
        </header>
        <?php
            include("db.php");

            $update = $_POST["update"];
            $title = $_POST["new-title"];
            $isbn = $_POST["new-isbn"];
            $author = $_POST["new-author"];
            $publication = $_POST["new-publication"];

            $query = "update books_info set ISBN='$isbn',TITLE='$title',AUTHOR_NAME='$author',PUBLISHER_NAME='$publication'  where ISBN='$update'";
            $result = mysqli_query($db,$query);
        ?>

        <div class="content">
            <h1 class ="feedbak">
                Book Info Updated Successfully!!
            </h1>
        </div>
    </div>
</body>
</html>