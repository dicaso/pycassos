import { Component, OnInit, Inject } from '@angular/core';
import { DOCUMENT, DomSanitizer } from '@angular/platform-browser';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'app-dosage',
  templateUrl: './dosage.component.html',
  styleUrls: ['./dosage.component.scss']
})
export class DosageComponent implements OnInit {
    gene: string;
    ploturl: string;
    originlocation: string;
    
    constructor(
	@Inject(DOCUMENT) document: any,
	private sanitizer: DomSanitizer,
	private route: ActivatedRoute,
	private router: Router
    ) {
	this.originlocation = document.location.origin;
    }

    ngOnInit() {
	//this.gene$ = this.route.paramMap
	//    .switchMap((params: ParamMap) => params.get('gene'))
	this.gene = this.route.snapshot.paramMap.get('gene');
	this.ploturl = this.originlocation + '/rest/dosage/' + this.gene;
    }

    sanitize(url:string) {
	return this.sanitizer.bypassSecurityTrustResourceUrl(url);
	//or with bypassSecurityTrustUrl
    }

}
