<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateServerStatusesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('server_statuses', function (Blueprint $table) {
            $table->bigIncrements('id');

            $table->unsignedBigInteger('server_id');
            $table->foreign('server_id')->references('id')->on('servers');

            $table->text('content');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('server_statuses');
    }
}
