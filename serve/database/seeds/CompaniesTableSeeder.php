<?php

use Illuminate\Database\Seeder;

class CompaniesTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        App\Models\Company::create([
            'user_id' => 1,
            'mID' => Str::uuid(),
            'name' => 'Mitrix Soluções',
        ]);
    }
}
