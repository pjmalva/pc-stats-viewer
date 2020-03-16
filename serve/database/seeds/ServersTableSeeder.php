<?php

use Illuminate\Database\Seeder;

class ServersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        App\Models\Server::create([
            'cID' => Str::uuid(),
            'company_id' => 1,
            'name' => 'Backupserver',
        ]);
    }
}
