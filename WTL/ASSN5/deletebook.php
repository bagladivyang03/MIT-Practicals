<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>deletebook</title>
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
                        <a href="displaybooks.php" class="user-nav__link">
                            View Books
                        </a>
                    </li>
                    <li class="user-nav__item">
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
        <div class="content">
            <form action="removedbooks.php" class="book-form" method = "post">
                <div class = "head">
                    <h1>Delete Book</h1>
                    <p>Delete Books from the database according to ISBN</p>
                    <hr>
                </div>

                <div class="book-container">

                    <div class="form-element">
                        <label for="isbn"><b>ISBN</b></label>
                        <input type="text" placeholder="Enter ISBN of the book" name="delete" id="delete" maxlength=30 required>
                    </div>

                    <div class="form-element">
                        <button type="submit" class="submitbtn" name="submit">Delete Book</button>
                    </div>

                    <div class="form-element">
                        <input type="reset" value="Reset">
                    </div>
                </div>
            </form>
        </div>
    </div>
</body>
</html>