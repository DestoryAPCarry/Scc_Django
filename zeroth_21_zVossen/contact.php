<?php
// Free html5 templates : www.zerotheme.com

$text = "<span style='color:red; font-size: 35px; line-height: 40px; magin: 10px;'>Error! Please try again.</span>";

if(isset($_POST['name']))
{
	$name=$_POST['name'];
	$email=$_POST['email'];
	$message=$_POST['message'];

	$to = "youremail@gmail.com";
	$subject = "Zerotheme - Testing Contact Form";
	$message = " Name: " . $name ."\r\n Email: " . $email . "\r\n Message:\r\n" . $message;
	 
	$from = "Zerotheme";
	$headers = "From:" . $from . "\r\n";
	$headers .= "Content-type: text/plain; charset=UTF-8" . "\r\n"; 
	 
	if(@mail($to,$subject,$message,$headers))
	{
	  $text = "<span style='color:blue; font-size: 35px; line-height: 40px; margin: 10px;'>Your Message was sent successfully !</span>";
	}
}
?>

<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6" lang="en"> <![endif]-->
<!--[if IE 7 ]><html class="ie ie7" lang="en"> <![endif]-->
<!--[if IE 8 ]><html class="ie ie8" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--><html lang="en"> <!--<![endif]-->
<head>

    <!-- Basic Page Needs
  ================================================== -->
	<meta charset="utf-8">
	<title>zVossen</title>
	<meta name="description" content="Free Responsive Html5 Css3 Templates | zerotheme.com">
	<meta name="author" content="www.zerotheme.com">
	
    <!-- Mobile Specific Metas
  ================================================== -->
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    
    <!-- CSS
  ================================================== -->
  	<link rel="stylesheet" href="css/zerogrid.css">
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="css/responsive.css">
	
	<!--[if lt IE 8]>
       <div style=' clear: both; text-align:center; position: relative;'>
         <a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
           <img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
        </a>
      </div>
    <![endif]-->
    <!--[if lt IE 9]>
		<script src="js/html5.js"></script>
		<script src="js/css3-mediaqueries.js"></script>
	<![endif]-->
    
</head>
<body id="single">
<div class="wrap-body">

<!--////////////////////////////////////Header-->
<header>
	<div class="top-bar">
		<div class="wrap-top zerogrid">
			<div class="row ">
				<div class="col-1-2">
					<div class="wrap-col">
						<div class="top-social">
							<a href="#"><img src="images/facebook.png" title="facebook"/></a>
							<a href="#"><img src="images/twitter.png" title="twitter"/></a>
							<a href="#"><img src="images/google.png" title="google"/></a>
							<a href="#"><img src="images/pinterest.png" title="pinterest"/></a>
							<a href="#"><img src="images/instagram.png" title="instagram"/></a>
						</div>
					</div>
				</div>
				<div class="col-1-2 ">
					<div class="wrap-col f-right">
						<ul>
							<li class="mail"><p>ContacUst@Gmail.com</p></li>
							<li class="phone"><p>80 88888 7</p></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="nav-bar">
		<div class="wrap-nav zerogrid">
			<div class="row">
				<div class="col-1-3">
					<div class="wrap-col">
						<div class="logo"><a href="#"><img src="images/logo.png"/></a></div>	
					</div>
				</div>
				<div class="col-2-3">
					<div class="wrap-col f-right">
						<div id="menu">
							<nav>
							   <ul>
								 <li><a href="index.html">Home</a></li>
								 <li><a href="archive.html">Blog</a></li>
								 <li><a href="single.html">About Us</a></li>
								 <li class="active"><a href="contact.html">Contact</a></li>
							   </ul>
							</nav>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="wrap-header">
		<h1>see the word differently</h1>
		<span>Request,design and book travel experiences as unique as you are</span>
		<center><div class="search-form">
			<form method="get" action="/search" id="search" class="f-right">
				<input name="q" type="text" size="40" placeholder="Where are you going ?" />
				<input type="submit" name="Submit" value="Search">
			</form>
		</div></center>
		<div id="top-destination">
			<nav>
				<ul>
					<li class="first"><p>Top Destination :</p></li>
					<li><a href="#">Paris</a></li>
					<li><a href="#">New York</a></li>
					<li><a href="#">London</a></li>
					<li><a href="#">Rome</a></li>
					<li><a href="#">San Francisco</a></li>
					<li class="last"><a href="#">More...</a></li>
				</ul>
			</nav>
		</div>
	</div>
</header>


<!--////////////////////////////////////Container-->
<section id="container">
	<div class="wrap-container">
		<div id="main-content">
			<div class="zerogrid">
				<div class="row wrap-content">
					<div class="col-3-4">
						<div class="wrap-col">
							<div class="contact">
								<h2>Contact</h2>
								
								<!--Warning-->
								<center><?php echo $text;?></center>
								<!---->
								
								<div id="contact_form">
									<form name="form1" id="ff" method="post" action="contact.php">
										<label>
										<span>Enter your name:</span>
										<input type="text"  name="name" id="name" required>
										</label>
										<label>
										<span>Enter your email:</span>
										<input type="email"  name="email" id="email" required>
										</label>
										<label>
										<span>Your message here:</span>
										<textarea name="message" id="message"></textarea>
										</label>
										<center><input class="sendButton" type="submit" name="Submit" value="Submit"></center>
									</form>
								</div>
							</div>
						</div>
					</div>
					<div class="col-1-4">
						<div id="sidebar" class="wrap-col">
							<div class="wrap-sidebar">
								<div class="widget">
									<div class=" wid-about">
										<a href="single.html">About us</a>
									</div>
									<div class="widget-box wid-tags">
										<div class="widget-title">
											<h5>Tags</h5>
										</div>
										<div class="widget-content">
											<a href="#">animals ,</a>
											<a href="#">cooking ,</a>
											<a href="#">countries ,</a>
											<a href="#">home ,</a>
											<a href="#">likes ,</a>
											<a href="#">photo ,</a>
											<a href="#">travel ,</a>
											<a href="#">video </a>
										</div>
									</div>
									<div class="widget-box wid-news">
										<div class="widget-title">
											<h5>TRENDING NEWS</h5>
										</div>
										<div class="widget-content">
											<div class="row">
												<div class="col-1-4">
													<div class="wrap-col">
														<a href="#"><img src="images/5.jpg" /></a>
													</div>
												</div>
												<div class="col-3-4">
													<div class="wrap-col">
														<a href="#">An Cozy Coffee Shop In The Centre Of The City </a>
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col-1-4">
													<div class="wrap-col">
														<a href="#"><img src="images/2.jpg" /></a>
													</div>
												</div>
												<div class="col-3-4">
													<div class="wrap-col">
														<a href="#">Partner up: The fellowship of fitness </a>
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col-1-4">
													<div class="wrap-col">
														<a href="#"><img src="images/4.jpg" /></a>
													</div>
												</div>
												<div class="col-3-4">
													<div class="wrap-col">
														<a href="#">Best and worst exercises to do when you have a cold </a>
													</div>
												</div>
											</div>
											<div class="row">
												<div class="col-1-4">
													<div class="wrap-col">
														<a href="#"><img src="images/12.jpg" /></a>
													</div>
												</div>
												<div class="col-3-4">
													<div class="wrap-col">
														<a href="#">Yoga for Rheumatoid Arthritis: Stretching Your Stiffness Away </a>
													</div>
												</div>
											</div>
										</div>
									</div>
									<div class="widget-box wid-archives">
										<div class="widget-title">
											<h5>Archives</h5>
										</div>
										<div class="widget-content">
											<select>
												<option value="audi" selected>Select Month</option>
												<option value="volvo">March 2015</option>
												<option value="saab">Febuary 2015</option>
												<option value="vw">VW</option>
											</select>
										</div>
									</div>
									<div class="widget-box wid-gallery">
										<div class="widget-title">
											<h5>Gallery</h5>
										</div>
										<div class="widget-content">
											<div class="col-1-3">
												<a href="#"><img src="images/1.jpg"></a>
												<a href="#"><img src="images/2.jpg"></a>
												<a href="#"><img src="images/12.jpg"></a>
												<a href="#"><img src="images/3.jpg"></a>
											</div>
											<div class="col-1-3">
												<a href="#"><img src="images/5.jpg"></a>
												<a href="#"><img src="images/15.jpg"></a>
												<a href="#"><img src="images/7.jpg"></a>
												<a href="#"><img src="images/16.jpg"></a>
											</div>
											<div class="col-1-3">
												<a href="#"><img src="images/8.jpg"></a>
												<a href="#"><img src="images/10.jpg"></a>
												<a href="#"><img src="images/4.jpg"></a>
												<a href="#"><img src="images/11.jpg"></a>
											</div>
											<div class="clear"></div>
										</div>
									</div>
									<div class="widget-box wid-meta">
										<div class="widget-title">
											<h5>Meta</h5>
										</div>
										<div class="widget-content">
											<ul>
												<li><a href="#">> May 2015</a></li>
												<li><a href="#">> May 2015</a></li>
												<li><a href="#">> May 2015</a></li>
												<li><a href="#">> May 2015</a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!--////////////////////////////////////Footer-->
<footer>
	<div class="zerogrid">
		<div class="wrap-footer">
			<div class="row">
				<div class="col-1-3">
					<div class="wrap-col">
						<div class="logo"><a href="#"><img src="images/logo2.png"/></a></div>
						<p>Nam libero tempore, cum soluta nobis est eligendi optio cumque quod maxime placeat cum soluta nobis
						facere possimus nihil impedit quo minus id quod maxime placeat facere possimus. est eligendi optio cumque</p>
						<p>facere possimus nihil impedit quo minus id quod maxime placeat facere possimus.</p>
					</div>
				</div>
				<div class="col-1-3">
					<div class="wrap-col">
						<div class="widget-title">
							<h5>News Letter</h5>
						</div>
						<p>facere possimus nihil impedit quo minus id quod maxime placeat facere possimus. est eligendi</p>
						<div class="subcribe-form" >
							<form method="get" action="/search" id="subcribe">
							  <input name="q" type="text" size="40" placeholder="Enter your email address...  " />
							</form>
						</div>
						<a class="button button03" href="#">Subcribe Now</a>
					</div>
				</div>
				<div class="col-1-3">
					<div class="wrap-col">
						<div class="widget-title">
							<h5>Flickr Widget</h5>
						</div>
						<div class="row">
							<div class="col-1-4">
								<div class="wrap-col">
									<a href="#"><img src="images/2.jpg" /></a>
								</div>
							</div>
							<div class="col-1-4">
								<div class="wrap-col">
									<a href="#"><img src="images/3.jpg" /></a>
								</div>
							</div>
							<div class="col-1-4">
								<div class="wrap-col">
									<a href="#"><img src="images/4.jpg" /></a>
								</div>
							</div>
							<div class="col-1-4">
								<div class="wrap-col">
									<a href="#"><img src="images/5.jpg" /></a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="bottom-footer">
		<div class="wrap-bottom">
			<div class="copyright">
				©2015 - More Templates <a href="http://www.cssmoban.com/" target="_blank" title="模板之家">模板之家</a> - Collect from <a href="http://www.cssmoban.com/" title="网页模板" target="_blank">网页模板</a>
			</div>
		</div>
	</div>
</footer>


</div>
</body></html>