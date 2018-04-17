import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
    scrollPosition: number;
    navpages: any[];
    
    constructor() {
	this.navpages = [
	    ['Home','home'],
	    ['Dosage sensitivity','dosage']
	];

    }
    
    ngOnInit() {
    }

}
