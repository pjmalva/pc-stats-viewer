<?php

namespace App\Http\Resources\Complete;

use Illuminate\Http\Resources\Json\JsonResource;
use App\Models\Company;
use App\Models\Server;

class ServerStatus extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return array
     */
    public function toArray($request)
    {
        return [
            'mID' => $this->mID,
            'cID' => $this->cID,
            'date' => $this->date,
            'disk' => $this->disk,
            'memory' => $this->memory,
            'network' => $this->network,
            'cpu' => $this->cpu,
            'proccess' => $this->proccess,
            'company' => Company::where('mID',$this->mID )->first(),
            'server' => Server::where('cID', $this->cID)->first(),
        ];
    }
}
