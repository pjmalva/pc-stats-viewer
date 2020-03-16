<?php

use Illuminate\Database\Seeder;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        App\User::create([
            'name' => 'Pj Malva',
            'email' => 'pjmalva@gmail.com',
            'password' => bcrypt('01757d1c75e4d37dd6b7a7af1485e2b7'),
        ]);
    }
}
