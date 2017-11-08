
<!DOCTYPE HTML>
<html>
	<head>
		<title>La lista de los datos olvidados</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<link rel="stylesheet" type="text/css" href="assets/css/stylepagination.css">
		<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> -->
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
			}
			
		</style>

	</head>
	<body>


		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<h1><a href="pagina.php">La lista de los datos olvidados</a></h1>
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
						<select name="ordenar"> 
							<option>Ordenar por ...</option>
							<option>Ordenar por nombre</option> 

							<option>Ordenar por fecha</option> 
						</select> 
						<!-- Post -->

						
							

							<?php		
						//Proceso de conexión con la base de datos
							$conex= mysql_connect("localhost","root","")
								or die("No se pudo realizar la conexion");
							mysql_select_db("taller",$conex)
								or die("ERROR con la base de datos");
							
							mysql_set_charset('utf8');

							$sql = "SELECT * FROM scraping";
							$records= mysql_query($sql);

							$row_cnt = mysql_num_rows($records);
							if ($row_cnt == 0) {
								echo "<article class='post'>
									<h2>No se encontraron datos</h2>
								</article>";
							}


						?>

							<?php

							while ($employ = mysql_fetch_assoc($records)) {

								

								echo "<article class='post'>
								<header>
									<div class='title'>
										<h2><a href='".$employ['link_com']."'>".$employ['nombre']."</a></h2>
									</div>
									<div class='meta'>
										<time class='published'>".$employ['fecha']."</time>
										<p>Fecha publicacion en esta pagina:</p>
										<p>".$employ['fecharegpag']."</p>
									</div>
								</header>";
								
								$img="SELECT * FROM imagenes WHERE id_sc=".$employ['id'];
								$exec= mysql_query($img);
								$rowimg = mysql_num_rows($exec);
								if ($rowimg ==0) {
								}
								else {

									while($image = mysql_fetch_assoc($exec)) { 
										echo "<a class='image featured'><img src='".$image['img']."' alt='Imagen de venta' /></a>";
										
									}
								}
								echo "
								<b>".$employ['publicacion']."</b><br><br>
								<p>".$employ['descripcion']."<p> 
								<p><b>Precio:</b>".' '." ".$employ['precio']."</p>
								<a href='".$employ['link_com']."'>Comunicar</a>
								

							</article>";

							}



							?>
						<!-- Pagination -->
						<center>
							<div class="pagination">
								<li>
									<a href="#" aria-label="Previous">
										<span aria-hidden="true">&laquo;</span>
									</a>
								</li>
								<li><a href="#">1</a></li>
								<li><a href="#">2</a></li>
								<li><a href="#">3</a></li>
								<li><a href="#">4</a></li>
								<li><a href="#">5</a></li>
								<li>
									<a href="#" aria-label="Next"> 
										<span aria-hidden="true">&raquo;</span>
									</a>
								</li>
							</div>
						</center>



					</div> &nbsp;

				<!-- Sidebar -->
					<section id="sidebar">

						<!-- Intro -->
							<section id="intro">
								<a href="pagina.php" class="logo"><img src="images/logo.png" alt="" /></a>
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