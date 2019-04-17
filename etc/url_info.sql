CREATE TABLE `shortened_url` (
  `mm_cod` varchar(10) NOT NULL,
  `original_url` varchar(255) NOT NULL,
  `total_clicks` int(11) NOT NULL,
  `new_url` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Indexes for table `shortened_url`
--
ALTER TABLE `shortened_url`
  ADD PRIMARY KEY (`mm_cod`);
COMMIT;