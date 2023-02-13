/// @description Insert description here
// You can write your code in this editor

draw_set_font(font_text);
draw_set_halign(fa_center);
draw_set_valign(fa_center);

#region draw grid
	draw_set_color(c_white);
	
	//draw x axis
	draw_line(0,288,576,288);
	for (i = 0; i<9; i++) {
		draw_line(32+(i*64),288-16,32+(i*64),288+16);	
		draw_text(32+(i*64),288+24,(i-4));
	}
	
	//draw y axis
	draw_line(288,0,288,576);
	for (i = 0; i<9; i++) {
		draw_line(288-16,32+(i*64),288+16,32+(i*64));
		draw_text(288-24,32+(i*64),-(i-4));
	}
	
#endregion

function drawVector(vecX,vecY,vecN) {
	draw_arrow(x,y,x+(vecX*64),y-(vecY*64),20);
	if (sign(vecY) < 0) {
		draw_text(x+(vecX*64),y-(vecY*64)+16,vecN);
	} else {
		draw_text(x+(vecX*64),y-(vecY*64)-16,vecN);
	}
}

#region draw vectors
	for (i = 0; i < array_length(resVec); i++) {
		draw_set_color(make_color_hsv(0+(48*i),255,255));
		drawVector(vec[i][0],vec[i][1],vecName[i]);
	}
	draw_set_color(c_white);
#endregion
