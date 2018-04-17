import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DosageComponent } from './dosage/dosage.component';

const routes: Routes = [
    { path: '',
      redirectTo: '/home',
      pathMatch: 'full'
    },
    { path: 'home', component: HomeComponent },
    { path: 'dosage/:gene', component: DosageComponent },
    //{ path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
