
<?php 

require_once("PHPPaging.lib/PHPPaging.lib.php");
require_once("conexion/conexion.php");
$pagina = new PHPPaging;

?>
<!DOCTYPE HTML>
<html>
	<head>
		<title>La lista de los datos olvidados</title>
		<meta charset="utf8">
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
						<h1><a href="index.php">La lista de los datos olvidados</a></h1>
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

						<!-- Post -->

							<?php
							$pagina->agregarConsulta("select * from scraping");
							$pagina->ejecutar();
							while($res=$pagina->fetchResultado()){
								$nombre=$res["nombre"];
								$fecha=$res["fecha"];
								$descripcion=$res["descripcion"];
								$precio = $res["precio"];

							
							//while ($employ = mysql_fetch_assoc($records)) {

								echo "<article class='post'>
								<header>
									<div class='title'>
										<h2><a href='#'>".$nombre."</a></h2>
									</div>
									<div class='meta'>
										<time class='published'>".$fecha."</time>
										
									</div>
								</header>
								<a href='#' class='image featured'><img src='' alt='Imagen de venta' /></a>
								<p>".$descripcion."<br> Precio:".' '." ".$precio."</p>
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
							<ul class="pagination" style="font-size: 20px;">
								<h4><center>Paginas:&nbsp;&nbsp;&nbsp;<?php echo $pagina->fetchNavegacion();  ?></center></h4>
								<h5><center>Te encuentras en la pagina:&nbsp;&nbsp;&nbsp;<?php echo $pagina->numEstaPagina () ;  ?></center></h5>
								

							</ul>

					</div> &nbsp;

				<!-- Sidebar -->
					<section id="sidebar">

						<!-- Intro -->
							<section id="intro">
								<a href="index.php" class="logo"><img src="images/logo.png" alt="" /></a>
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