CREATE TABLE `user_login` (
  `id` int(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `full_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `user_login` (`id`, `email`, `password`, `full_name`) VALUES
(1, 'craig@myserver.com', 'password', 'Craig');


ALTER TABLE `user_login`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `user_login`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

CREATE USER 'greg\@gmail.com'@'localhost' IDENTIFIED BY 'greg';
GRANT ALL PRIVILEGES ON *.* TO 'tolkien'@'%';
GRANT ALL PRIVILEGES ON videoapp.* TO 'greg\@gmail.com'@'localhost';

SELECT full_name FROM user_login WHERE email = 'greg@myserver.com'

SELECT * FROM `user_login` WHERE email = 'greg@myserver.com' AND password = 'password';