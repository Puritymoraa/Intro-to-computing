#####################################################################
# Original Author: Purity Moraa Kinaro
# Program that incoorporates turtles, functions and a conditional statement to tell a story about love
#####################################################################

marry = input("Will you marry me?")
if marry == "Yes":          #If she says 'yes' then show the entire marriage proposal
    import turtle
    import random
    wn = turtle.Screen()
    wn.bgcolor("Lightblue")  
    wn.addshape("man_ring.gif")
    # This image is downloaded from; https://www.bing.com/images/search?view=detailV2&ccid=29OUwDH7&id=425247F9B1715C8A594C0780117EA2E413720924&thid=OIP.29OUwDH7TtNhf-rAAoLeZQHaIi&mediaurl=https%3a%2f%2fmedia.gettyimages.com%2fillustrations%2fman-proposing-on-one-knee-with-a-diamond-ring-illustration-id85470585%3fs%3d612x612&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.dbd394c031fb4ed3617feac00282de65%3frik%3dJAlyE%252bSifhGABw%26pid%3dImgRaw%26r%3d0&exph=612&expw=531&q=Man+With+a+ring+Animated&simid=608031584196036966&FORM=IRPRST&ck=1C9846AC7F6F065190DB6CB6FEAA30BE&selectedIndex=0&ajaxhist=0&ajaxserp=0
    wn.addshape("proposal_image_man.gif")
    # This image is downloaded from;https://www.bing.com/images/search?view=detailV2&ccid=U8ugFCdd&id=58F61C9F97EFE336687B42163C0C7F304F4CEDA7&thid=OIP.U8ugFCddw1x7MbEwrVffHQHaG1&mediaurl=https%3a%2f%2fwww.pngarts.com%2ffiles%2f3%2fWedding-PNG-Image-with-Transparent-Background.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.53cba014275dc35c7b31b130ad57df1d%3frik%3dp%252b1MTzB%252fDDwWQg%26pid%3dImgRaw%26r%3d0&exph=1522&expw=1648&q=png+images+of+%22will+you+marry+me%3f%22&simid=608034251373957233&FORM=IRPRST&ck=E8BEEEEDA6FFCC4D438FF981F1638623&selectedIndex=20&ajaxhist=0&ajaxserp=0
    wn.addshape("will_you_marry_me.gif")
    # This image is downloaded from;https://www.bing.com/images/search?view=detailV2&ccid=FRD0brbY&id=362FF56827975BE8F471E308CDE9BAA0DFCC5F60&thid=OIP.FRD0brbYWUTth-5QhjerlwHaC9&mediaurl=https%3a%2f%2fmarry-me.at.ua%2fLOGO.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.1510f46eb6d85944ed87ee508637ab97%3frik%3dYF%252fM36C66c0I4w%26pid%3dImgRaw%26r%3d0&exph=1200&expw=3000&q=png+images+of+%22will+you+marry+me%3f%22&simid=608048553609221522&FORM=IRPRST&ck=0C8F17859CB8AD1A955919435644603B&selectedIndex=9&ajaxhist=0&ajaxserp=0
    wn.addshape("heart_yes.gif")
    # This image is downloaded from;https://www.bing.com/images/search?view=detailV2&ccid=Ey%2fS5I3l&id=B7A37B14FF8AC142BC54D4CA6B6BB9A05958B8E3&thid=OIP.Ey_S5I3lvBOVHsMY35RztwHaGc&mediaurl=https%3a%2f%2fclipart.info%2fimages%2fccovers%2f1522851754Red-Heart-PNG-Clipart.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.132fd2e48de5bc13951ec318df9473b7%3frik%3d47hYWaC5a2vK1A%26pid%3dImgRaw%26r%3d0&exph=4353&expw=5000&q=png+images+of+a+red+heart&simid=608039572838297759&FORM=IRPRST&ck=500CE7199EB90543DE2EB996CC9BF5C6&selectedIndex=0&ajaxhist=0&ajaxserp=0
    wn.addshape("heart_broken.gif")
    # This image is downloaded from; https://www.bing.com/images/search?view=detailV2&ccid=QSvpiY2B&id=A743DB351D592B8994273558FEB464FDE028C40C&thid=OIP.QSvpiY2BJFX86Nw4TENb4gHaGl&mediaurl=https%3a%2f%2fclipart.info%2fimages%2fccovers%2f1484751733broken-heart-png-image.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.412be9898d812455fce8dc384c435be2%3frik%3dDMQo4P1ktP5YNQ%26pid%3dImgRaw%26r%3d0&exph=1307&expw=1469&q=free+png+images+of+a+broken+heart&simid=607993397677720993&FORM=IRPRST&ck=666C608633D01EA62E1FA6B3FA6CDCB0&selectedIndex=0&ajaxhist=0&ajaxserp=0

    def cloud():
        clouds = turtle.Turtle() # Make a background with a clouds
        clouds.speed(0)
        clouds.pensize(5)
        clouds.hideturtle()
        clouds.penup()
        x = random.randrange(-500, 500)
        clouds.goto(x, 100)
        clouds.pendown()
        for i in range(10):
            clouds.circle(20, 180)
            clouds.right(160)
            clouds.end_fill()
        clouds.right(200)
        clouds.forward(230)
    def man_propose():
        """ Man going to propose"""
        man = turtle.Turtle()
        man.hideturtle()
        man.penup()
        man.goto(-200, -150)
        man.showturtle()
        man.shape("man_ring.gif")
        man.speed(1)
        man.forward(200)
        man.hideturtle()
    
    def the_proposal():
        """ Asks for a hand in marriage"""
        proposal = turtle.Turtle()
        proposal.hideturtle()
        proposal.penup()
        proposal.goto(200, -150)
        proposal.showturtle()
        proposal.shape("proposal_image_man.gif")
        proposal.speed(1)
    
    def marry_me():
        """ The proposal sign is replaced by a big heart to
            show that she has accepted his proposal, love wins!!"""
        will_you = turtle.Turtle()
        will_you.hideturtle()
        will_you.penup()
        will_you.goto(200, 100)
        will_you.showturtle()
        will_you.shape("will_you_marry_me.gif")
        will_you.speed(1)
        will_you.shape("heart_yes.gif")
        
else:   #If the answer is other than Yes, display a broken heart.
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("Lightblue")
    wn.addshape("heart_broken.gif")
    broken_heart = turtle.Turtle()
    broken_heart.shape("heart_broken.gif")
    broken_heart.speed(1)
    
        

        
cloud()
cloud()
man_propose()
the_proposal()
marry_me()
wn.exitonclick()
