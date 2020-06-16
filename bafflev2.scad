scale=25.4;    // Inch to mm if necessary, use if sizing in mm, 25.4 if sizing in inches
dt=5.75*scale; // Inside diameter of the tube
t=.5*scale;     // Thickness of the baffle support
s=.5*scale;     //Support size
tt=(4/32)*scale; //Thickness of the baffle
bd=1.23*2*scale; //Baffle hole diameter
be=15; //contols the slope of the baffle support

dss=1.25*scale; //screw support
dsss=.25*scale; //screw hole in screw support

$fn=150;
difference(){
union(){
//baffle itself
translate([0,0,tt/2])
difference(){
    cylinder(h=tt, d=dt, center=true); //the disk
    translate([0,0,-tt/2]) cylinder(h=tt+10, d1=bd-30, d2=bd+30, center=true); // the baffle hole
}

//baffle support
translate([0,0,t/2])
difference(){
    cylinder(h=t, d=dt, center=true);
    cylinder(h=t+10, d1=(dt-s)-be, d2=(dt-s)+be,center=true);
}


//Screw support
for (i=[0:2])
rotate([0,0,i*120]){

intersection(){
translate([dt/2,0,t/2]) cylinder(h=t, d=dss, center=true);
cylinder(h=t+40, d=dt, center=true);
}


}

}
for (i=[0:2])
rotate([0,0,i*120]){
translate([dt/2-dss/4,0,t/2]) cylinder(h=4*t, d=dsss, center=true);
}
}


//__________________________________________________________
// Represents the desired baffle hole diameter
if(0){
// your baffle hole verifier
color( "blue" ) {
difference(){
    cylinder(h=50, d=bd, center=true);
    translate([0,0,-100]) cube(size=[200,200,200],center=false);
}
}

// your tube 
color( "red" ) {
    difference(){
    translate([0,0,-5]) cylinder(h=8, d=dt+5, center=true);
    cylinder(h=50, d=dt, center=true);
}
}
}
