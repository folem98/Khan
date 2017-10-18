<!DOCTYPE HTML>
<html>
	<head>
		<title>La lista de los datos olvidados</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<style type="text/css">
			.post > header .meta .published {
					color: #3c3b3b;
					display: block;
					font-family: "Raleway", Helvetica, sans-serif;
					font-size: 0.55em;
					font-weight: 800;
					letter-spacing: 0.25em;
					margin-top: 0.5em;
					text-transform: uppercase;
					white-space: nowrap;
		</style>
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
	</head>
	<body>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<h1><a href="#">La lista de los datos olvidados</a></h1>
						<nav class="main">
							<ul>
								<li class="search">
									<a class="fa-search" href="#search">Buscar</a>
									<form id="search" method="get" action="#">
										<input type="text" name="query" placeholder="Buscar" />
									</form>
								</li>

							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">
						<?php
						//Proceso de conexión con la base de datos
							$conex= mysql_connect("localhost","root","")
								or die("No se pudo realizar la conexion");
							mysql_select_db("taller",$conex)
								or die("ERROR con la base de datos");
							
							$sql = "SELECT * FROM scraping";
							$records= mysql_query($sql);
							$row_cnt = mysql_num_rows($records);
							if ($row_cnt == 0) {
								echo "<article class='post'>
									<h2>No se encontraron datos</h2>
								</article>";
							}


						?>

						<!-- Post -->

							<?php

							while ($employ = mysql_fetch_assoc($records)) {

								echo "<article class='post'>
								<header>
									<div class='title'>
										<h2><a href='#'>".$employ['nombre']."</a></h2>
									</div>
									<div class='meta'>
										<time class='published'>".$employ['fecha']."</time>
										
									</div>
								</header>
								<a href='#' class='image featured'><img src='' alt='Imagen de venta' /></a>
								<p>".$employ['descripcion']."<br> Precio:".' '." ".$employ['precio']."</p>
								<footer>
									<ul class='stats'>
										<li><a href='#'>General</a></li>
										<li><a href='#' class='icon fa-heart'>28</a></li>
										<li><a href='#' class='icon fa-comment'>128</a></li>
									</ul>
								</footer>

							</article>";




							}

							


							?>






						<!-- Pagination -->
							<ul class="actions pagination">
								<li><a href="#" class="disabled button big previous">Previous Page</a></li>
								<li><a href="#" class="button big next">Next Page</a></li>
							</ul>

					</div> &nbsp;

				<!-- Sidebar -->
					<section id="sidebar">

						<!-- Intro -->
							<section id="intro">
								<a href="#" class="logo"><img src="images/logo.png" alt="" /></a>
								<header>
									<h2>La lista de los datos olvidados</h2>
									<p>Another fine responsive site template in HTML5</a></p>
								</header>
							</section>

						

						<!-- About -->
							<section class="blurb">
								<h2>About</h2>
								<p>Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod amet placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus at phasellus sed ultricies.</p>
								<!-- <ul class="actions">
									<li><a href="#" class="button">Learn More</a></li>
								</ul> -->
							</section>

						<!-- Footer -->
							<section id="footer">
								<ul class="icons">
									<li><a href="#" class="fa-twitter"><span class="label">Twitter</span></a></li>
									<li><a href="#" class="fa-facebook"><span class="label">Facebook</span></a></li>
									<li><a href="#" class="fa-instagram"><span class="label">Instagram</span></a></li>
									<li><a href="#" class="fa-rss"><span class="label">RSS</span></a></li>
									<li><a href="#" class="fa-envelope"><span class="label">Email</span></a></li>
								</ul>
								<p class="copyright">&copy; Untitled. Crafted: <a href="http://designscrazed.org/">HTML5</a>.</p>
							</section>

					</section>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="assets/js/main.js"></script>

	</body>
</html>