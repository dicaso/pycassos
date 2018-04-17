import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dosage',
  templateUrl: './dosage.component.html',
  styleUrls: ['./dosage.component.scss']
})
export class DosageComponent implements OnInit {
    gene: string;
    
    constructor() { }

    ngOnInit() {
    }

}
