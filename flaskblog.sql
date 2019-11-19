-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 12, 2019 at 05:20 PM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `blog_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `img` varchar(30) NOT NULL,
  `body` varchar(2000) NOT NULL,
  `author` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`blog_id`, `title`, `img`, `body`, `author`) VALUES
(5, 'Bankcoin Website Terms of Use', '', 'Wen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n\r\nWhy do we use it?\r\nIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).\r\n\r\njj\r\n\r\n', 'arif mulla'),
(7, 'ifaceshare, Social Network Sharing Platform', '', '@app.route(\'/delete/<string:table>/<string:id>\', methods=[\'POST\'])\r\n@is_logged_in\r\ndef delete(table, id):\r\n  # Create Cursor\r\n  cur = mysql.connection.cursor()\r\n\r\n  # Execute\r\n  cur.execute(\"DELETE FROM %s WHERE id = %s\", (table, id))\r\n\r\n  mysql.connection.commit()\r\n\r\n  cur.close()\r\n\r\n  flash(\'%s deleted\'(table), \'success\')\r\n\r\n  return redirect(url_for(\'dashboard\'))', 'ansarul mulla'),
(8, 'Pypsum is an interface to lipsum.com written in Python Pypsum', '', 'Wrong Decision', 'arif mulla'),
(10, 'ifaceshare, Social Network Sharing Platform', '', '<div class=\"jumbotron jumbotron-sm\">\r\n    <div class=\"container\">\r\n        <div class=\"row\">\r\n            <div class=\"col-sm-12 col-lg-12\">\r\n                <h1 class=\"h1\">\r\n                    Contact us <small>Feel free to contact us</small></h1>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"container\">\r\n    <div class=\"row\">\r\n        <div class=\"col-md-8\">\r\n            <div class=\"well well-sm\">\r\n                <form method=\"POST\">\r\n                <div class=\"row\">\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                            <label for=\"name\">\r\n                                Name</label>\r\n                            <input type=\"text\" class=\"form-control\" id=\"name\" name=\"name\" placeholder=\"Enter name\" required=\"required\" />\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"email\">\r\n                                Email Address</label>\r\n                            <div class=\"input-group\">\r\n                                <span class=\"input-group-addon\"><span class=\"glyphicon glyphicon-envelope\"></span>\r\n                                </span>\r\n                                <input type=\"email\" name=\"email\" class=\"form-control\" id=\"email\" placeholder=\"Enter email\" required=\"required\" /></div>\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"subject\">\r\n                                Subject</label>\r\n                            <select id=\"subject\" name=\"subject\" class=\"form-control\" required=\"required\">\r\n                                <option value=\"na\" selected=\"\">Choose One:</option>\r\n                                <option value=\"service\">General Customer Service</option>\r\n                                <option value=\"suggestions\">Suggestions</option>\r\n                                <option value=\"product\">Product Support</opt', 'ansarul mulla'),
(11, 'ifaceshare, Social Network Sharing Platform', '', '<div class=\"btn btn-primary btn-sm float-left\">\r\n      <span>Choose file</span>\r\n      <input type=\"file\">\r\n    </div>', 'ansarul mulla'),
(67, 'New Blog ', '<FileStorage: \'%E2%80%AA%2B880', 'image', 'ansarul mulla'),
(68, 'New Blog ', '<FileStorage: \'%E2%80%AA%2B880', 'image', 'ansarul mulla'),
(69, 'New Blog ', '<FileStorage: \'%E2%80%AA%2B880', 'image', 'ansarul mulla'),
(70, 'New Blog ', '<FileStorage: \'bbb.jpg\' (\'imag', 'image', 'ansarul mulla');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(252) NOT NULL,
  `email` varchar(222) NOT NULL,
  `subject` varchar(250) NOT NULL,
  `msg` varchar(2222) NOT NULL,
  `author` varchar(222) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `subject`, `msg`, `author`) VALUES
(6, 'mariya 5555555', 'ansarul54300@gmail.com', 'aaaaaaaaaaaaaaaaaaa', '   Contact us Feel free to contact usTwitter, Inc.795 Folsom Ave, Suite 600San Francisco, CA 94107P: (123) 45 Contact us Feel free to contact usTwitter, Inc.795 Folsom Ave, Suite 600San Francisco, CA 94107P: (123) 456-78906-7890  h', 'arif mulla'),
(12, 'ansarul mulla', 'mdansarul543@gmail.com', 'service', '<div class=\"jumbotron jumbotron-sm\">\r\n    <div class=\"container\">\r\n        <div class=\"row\">\r\n            <div class=\"col-sm-12 col-lg-12\">\r\n                <h1 class=\"h1\">\r\n                    Contact us <small>Feel free to contact us</small></h1>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"container\">\r\n    <div class=\"row\">\r\n        <div class=\"col-md-8\">\r\n            <div class=\"well well-sm\">\r\n                <form method=\"POST\">\r\n                <div class=\"row\">\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                            <label for=\"name\">\r\n                                Name</label>\r\n                            <input type=\"text\" class=\"form-control\" id=\"name\" name=\"name\" placeholder=\"Enter name\" required=\"required\" />\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"email\">\r\n                                Email Address</label>\r\n                            <div class=\"input-group\">\r\n                                <span class=\"input-group-addon\"><span class=\"glyphicon glyphicon-envelope\"></span>\r\n                                </span>\r\n                                <input type=\"email\" name=\"email\" class=\"form-control\" id=\"email\" placeholder=\"Enter email\" required=\"required\" /></div>\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"subject\">\r\n                                Subject</label>\r\n                            <select id=\"subject\" name=\"subject\" class=\"form-control\" required=\"required\">\r\n                                <option value=\"na\" selected=\"\">Choose One:</option>\r\n                                <option value=\"service\">General Customer Service</option>\r\n                                <option value=\"suggestions\">Suggestions</option>\r\n                                <option value=\"product\">Product Support</option>\r\n                            </select>\r\n                        </div>\r\n                    </div>\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                       ', 'ansarul mulla'),
(13, 'ansarul mulla', 'mdansarul543@gmail.com', 'na', '<div class=\"jumbotron jumbotron-sm\">\r\n    <div class=\"container\">\r\n        <div class=\"row\">\r\n            <div class=\"col-sm-12 col-lg-12\">\r\n                <h1 class=\"h1\">\r\n                    Contact us <small>Feel free to contact us</small></h1>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"container\">\r\n    <div class=\"row\">\r\n        <div class=\"col-md-8\">\r\n            <div class=\"well well-sm\">\r\n                <form method=\"POST\">\r\n                <div class=\"row\">\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                            <label for=\"name\">\r\n                                Name</label>\r\n                            <input type=\"text\" class=\"form-control\" id=\"name\" name=\"name\" placeholder=\"Enter name\" required=\"required\" />\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"email\">\r\n                                Email Address</label>\r\n                            <div class=\"input-group\">\r\n                                <span class=\"input-group-addon\"><span class=\"glyphicon glyphicon-envelope\"></span>\r\n                                </span>\r\n                                <input type=\"email\" name=\"email\" class=\"form-control\" id=\"email\" placeholder=\"Enter email\" required=\"required\" /></div>\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"subject\">\r\n                                Subject</label>\r\n                            <select id=\"subject\" name=\"subject\" class=\"form-control\" required=\"required\">\r\n                                <option value=\"na\" selected=\"\">Choose One:</option>\r\n                                <option value=\"service\">General Customer Service</option>\r\n                                <option value=\"suggestions\">Suggestions</option>\r\n                                <option value=\"product\">Product Support</option>\r\n                            </select>\r\n                        </div>\r\n                    </div>\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                       ', 'ansarul mulla'),
(14, 'ansarul mulla', 'mdansarul543@gmail.com', 'na', '<div class=\"jumbotron jumbotron-sm\">\r\n    <div class=\"container\">\r\n        <div class=\"row\">\r\n            <div class=\"col-sm-12 col-lg-12\">\r\n                <h1 class=\"h1\">\r\n                    Contact us <small>Feel free to contact us</small></h1>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"container\">\r\n    <div class=\"row\">\r\n        <div class=\"col-md-8\">\r\n            <div class=\"well well-sm\">\r\n                <form method=\"POST\">\r\n                <div class=\"row\">\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                            <label for=\"name\">\r\n                                Name</label>\r\n                            <input type=\"text\" class=\"form-control\" id=\"name\" name=\"name\" placeholder=\"Enter name\" required=\"required\" />\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"email\">\r\n                                Email Address</label>\r\n                            <div class=\"input-group\">\r\n                                <span class=\"input-group-addon\"><span class=\"glyphicon glyphicon-envelope\"></span>\r\n                                </span>\r\n                                <input type=\"email\" name=\"email\" class=\"form-control\" id=\"email\" placeholder=\"Enter email\" required=\"required\" /></div>\r\n                        </div>\r\n                        <div class=\"form-group\">\r\n                            <label for=\"subject\">\r\n                                Subject</label>\r\n                            <select id=\"subject\" name=\"subject\" class=\"form-control\" required=\"required\">\r\n                                <option value=\"na\" selected=\"\">Choose One:</option>\r\n                                <option value=\"service\">General Customer Service</option>\r\n                                <option value=\"suggestions\">Suggestions</option>\r\n                                <option value=\"product\">Product Support</option>\r\n                            </select>\r\n                        </div>\r\n                    </div>\r\n                    <div class=\"col-md-6\">\r\n                        <div class=\"form-group\">\r\n                       ', 'ansarul mulla');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `username` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `first_name`, `last_name`, `username`, `email`, `password`) VALUES
(1, 'ansarul', 'mulla', 'ansarul', 'mdansarul543@gmail.com', '11111'),
(40, 'arif', 'mulla', 'arifmulla', 'mdarifmulla@gmail.com', '11111'),
(44, 'mala', 'khatun', 'mala', 'mala@gmail.com', 'pbkdf2:sha256:150000$zO9L');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`blog_id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `blog_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
